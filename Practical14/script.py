import xml.dom.minidom as minidom
import xml.sax
import time

XML_FILE = 'C:\IBI-practical\IBI_2024-25\go_obo.xml'

# -------------------------------
# DOM Method
# -------------------------------

def parse_dom(xml_file):
    start = time.time()
    doc = minidom.parse(xml_file)
    terms = doc.getElementsByTagName("term")

    max_is_a = {
        "molecular_function": ("", 0),
        "biological_process": ("", 0),
        "cellular_component": ("", 0)
    }

    for term in terms:
        namespace = term.getElementsByTagName("namespace")[0].firstChild.nodeValue.strip()
        name = term.getElementsByTagName("name")[0].firstChild.nodeValue.strip()
        is_a_count = len(term.getElementsByTagName("is_a"))

        if namespace in max_is_a:
            if is_a_count > max_is_a[namespace][1]:
                max_is_a[namespace] = (name, is_a_count)

    end = time.time()
    dom_time = end - start
    print("DOM Results:")
    for ns, (term_name, count) in max_is_a.items():
        print(f"{ns}: \"{term_name}\" with {count} is_a references")
    print(f"DOM parsing took {dom_time:.4f} seconds\n")
    return dom_time, max_is_a


# -------------------------------
# SAX Method
# -------------------------------

class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_element = ""
        self.in_term = False

        self.namespace_buffer = ""
        self.name_buffer = ""
        self.is_a_count = 0

        self.max_is_a = {
            "molecular_function": ("", 0),
            "biological_process": ("", 0),
            "cellular_component": ("", 0)
        }

    def startElement(self, name, attrs):
        self.current_element = name
        if name == "term":
            self.in_term = True
            self.namespace_buffer = ""
            self.name_buffer = ""
            self.is_a_count = 0

    def characters(self, content):
        if not self.in_term:
            return
        if self.current_element == "namespace":
            self.namespace_buffer += content
        elif self.current_element == "name":
            self.name_buffer += content
        elif self.current_element == "is_a":
            
            self.is_a_count += 1

    def endElement(self, name):
        if name == "term":
            namespace = self.namespace_buffer.strip()
            term_name = self.name_buffer.strip()
            if namespace in self.max_is_a:
                if self.is_a_count > self.max_is_a[namespace][1]:
                    self.max_is_a[namespace] = (term_name, self.is_a_count)
            
            self.in_term = False
            self.namespace_buffer = ""
            self.name_buffer = ""
            self.is_a_count = 0
        self.current_element = ""



def parse_sax(xml_file):
    start = time.time()
    handler = GOHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(xml_file)
    end = time.time()
    sax_time = end - start

    print("SAX Results:")
    for ns, (term_name, count) in handler.max_is_a.items():
        print(f"{ns}: \"{term_name}\" with {count} is_a references")
    print(f"SAX parsing took {sax_time:.4f} seconds\n")
    return sax_time, handler.max_is_a


# -------------------------------
# Main Execution
# -------------------------------

if __name__ == "__main__":
    print("Parsing Gene Ontology XML...\n")

    dom_duration, dom_result = parse_dom(XML_FILE)
    sax_duration, sax_result = parse_sax(XML_FILE)

    # Validate equality of outputs
    print("Validation:")
    for ns in ["molecular_function", "biological_process", "cellular_component"]:
        dom_name, dom_count = dom_result[ns]
        sax_name, sax_count = sax_result[ns]
        if dom_count != sax_count:
            print(f"❌ Mismatch in {ns}: DOM={dom_count}, SAX={sax_count}")
        elif dom_name != sax_name:
            print(f"⚠️ Term name differs in {ns} (counts match):\n  DOM: \"{dom_name}\"\n  SAX: \"{sax_name}\"")
        else:
            print(f"✅ {ns}: term and count match")

    # Compare speed
    if dom_duration < sax_duration:
        print("\n# DOM was faster")
    elif sax_duration < dom_duration:
        print("\n# SAX was faster")
    else:
        print("\n# Both took the same time")
