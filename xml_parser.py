# Program Name: XML_Parser.py
# By Alicia Gallagher
# Date: 2/12/2014
# Purpose: script to read very large XML files that may contain invalid or badly formed XML.
# It is meant to read bibliographic data. It can splice out a set of records based on a record separator tag.
# To find the record separator tag, the script will print a list of tags found.
# The user can choose which tag to splice the records on.

from xml.sax.handler import ContentHandler
from xml.sax import make_parser, handler, SAXParseException
from xml.sax.saxutils import XMLGenerator
import sys


# -------------------------------------------------------------
class MyContentHandler(XMLGenerator): 
    def __init__(self):
        XMLGenerator.__init__(self, outfile, 'utf-8') #super constructor
        self.record_count = 0

    def setRecordSeparator(self, record_separator):
        self.record_separator = record_separator

    def setSpliceAmount(self, splice_amount):
        self.splice_amount = splice_amount
        
    def endElement(self, name):
        self._write(u'</%s>' % name)
        if name == self.record_separator:
            self.record_count+=1
        
        if self.record_count == self.splice_amount:
            raise SAXParseException("Splice amount reached!")
  
# MAIN --------------------------------------------------------
 
def get_tag_information(infile):

    print "Display tag information from the entire file"
    saxparser.parse(infile)
    
def splice_records(infile):
    print "Enter the record separator to splice on"
    record_separator = raw_input('> ')
    
    #pass the record separator to the my_handler object
    my_handler.setRecordSeparator(record_separator)
    
    print "Enter the amount of records to splice"
    splice_amount = int(raw_input('> '))
    
    #pass the splice_amount to the my_handler object
    my_handler.setSpliceAmount(splice_amount)
    
    try:
        #call the SAX parsing operation
        saxparser.parse(infile)
    except SAXParseException, message:
        print "Exception: ", message
    
    print "\nTotal Record count %d\n" % my_handler.record_count
    infile.close
    outfile.close
    
if __name__ == "__main__":
    #get args parameters from the command line.
    script, input_file = sys.argv
    
    #get the output file object
    outfile = open("spliced_file.xml", "w")
    
    #set up the XML Parser API
    my_handler = MyContentHandler()
    
    saxparser = make_parser()
    saxparser.setFeature(handler.feature_validation,False)
    saxparser.setFeature(handler.feature_external_ges, False)
    saxparser.setContentHandler(my_handler)
    
    #get the input file object
    infile = open(input_file, "r")
    

    #display a menu to the user.
    ans = True
    while ans:
        print "\nWelcome to marcxml_parser.py\n" 
        print "Please choose an option: "

        print("""
        1. Display all tags
        2. Splice some records to a new file

        Press ENTER to quit.
        """)

        ans = raw_input('> ')
        if ans == "1":
            get_tag_information(infile)
            ans = 0
        elif ans == "2":
            splice_records(infile)
            ans = 0
        elif ans!= "":
            print("\nNot a valid choice")




