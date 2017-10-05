from common_functions import *

#Goes at the start of the graphml file, currently goes in the middle after the nodes, I need to fix this.
start = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\n<graphml xmlns=\"http://graphml.graphdrawing.org/xmlns\" xmlns:java=\"http://www.yworks.com/xml/yfiles-common/1.0/java\" xmlns:sys=\"http://www.yworks.com/xml/yfiles-common/markup/primitives/2.0\" xmlns:x=\"http://www.yworks.com/xml/yfiles-common/markup/2.0\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:y=\"http://www.yworks.com/xml/graphml\" xmlns:yed=\"http://www.yworks.com/xml/yed/3\" xsi:schemaLocation=\"http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd\">\n  <!--Created by yEd 3.15.0.2-->\n  <key attr.name=\"Description\" attr.type=\"string\" for=\"graph\" id=\"d0\"/>\n  <key for=\"port\" id=\"d1\" yfiles.type=\"portgraphics\"/>\n  <key for=\"port\" id=\"d2\" yfiles.type=\"portgeometry\"/>\n  <key for=\"port\" id=\"d3\" yfiles.type=\"portuserdata\"/>\n  <key attr.name=\"url\" attr.type=\"string\" for=\"node\" id=\"d4\"/>\n  <key attr.name=\"description\" attr.type=\"string\" for=\"node\" id=\"d5\"/>\n  <key for=\"node\" id=\"d6\" yfiles.type=\"nodegraphics\"/>\n  <key for=\"graphml\" id=\"d7\" yfiles.type=\"resources\"/>\n  <key attr.name=\"url\" attr.type=\"string\" for=\"edge\" id=\"d8\"/>\n  <key attr.name=\"description\" attr.type=\"string\" for=\"edge\" id=\"d9\"/>\n  <key for=\"edge\" id=\"d10\" yfiles.type=\"edgegraphics\"/>\n  <graph edgedefault=\"directed\" id=\"G\">\n"
#Goes at the end of the document
end = "  </graph>\n  <data key=\"d7\">\n    <y:Resources/>\n  </data>\n</graphml>"
connection = 0
nodes = []

def find_our_device(line):
	return line.split(",")[0]
#find Neighbor's IP from resultes.txt
def find_neighbor(line):
	temp = line
	return temp.split(",")[1]

def find_our_int(line):
	temp = line
	return temp.split(",")[2]
def find_their_int(line):
	temp = line
	return temp.split(",")[3]

#Reads in the connections from the resultes.txt file
def read_in_conn(input,connection):
	for line in open(input, 'r').readlines():
		this_dev_ip =  find_our_device(line)
		neighbor_ip = find_neighbor(line)
		#print (connection)
		this_int = find_our_int(line)
		their_int=find_their_int(line)
		make_conn(neighbor_ip,this_dev_ip,this_int,their_int,connection)
		connection = connection+1
#Reads in the individual nodes from the file
def read_node(input):
	for line in open(input, 'r').readlines():
		this_dev_ip =  find_our_device(line)
		neighbor_ip = find_neighbor(line)
		make_node(neighbor_ip)
		make_node(this_dev_ip)

#the xml code to make the Connection		
def make_conn(ip1,ip2,int_one,int_two,connection):
	#print (ip1+ " "+ip2)
	tmp = str(connection)
	to_doc_a(file_name,"<edge id=\"e")
	to_doc_a(file_name,tmp)
	to_doc_a(file_name,"\" source=\"")
	#Node name: one side of the connection
	to_doc_a(file_name,ip1)
	to_doc_a(file_name,"\" target=\"")
	#Node name: other side of the connection
	to_doc_a(file_name,ip2)
	big_line_one = """\">")
	<data key=\"d9\"/>")
	  <data key=\"d10\">")
	    <y:PolyLineEdge>")
	      <y:Path sx=\"0.0\" sy=\"0.0\" tx=\"0.0\" ty=\"0.0\"/>
	      <y:LineStyle color=\"#000000\" type=\"line\" width=\"1.0\"/>
	      <y:Arrows source=\"none\" target=\"standard\"/>
	      <y:EdgeLabel alignment=\"center\" configuration=\"AutoFlippingLabel\" distance=\"2.0\" fontFamily=\"Dialog\" fontSize=\"12\" fontStyle=\"plain\" hasBackgroundColor=\"false\" hasLineColor=\"false\" height=\"18.701171875\" modelName=\"custom\" preferredPlacement=\"anywhere\" ratio=\"0.5\" textColor=\"#000000\" visible=\"true\" width=\"27.337890625\" x=\"44.115836688217826\" y=\"23.016682857619458\">
		  """
	#One of the interfaces so the connection is labled
	to_doc_a(file_name,big_line_one)
	to_doc_a(file_name,int_one)
	to_doc_a(file_name,"  ")
	#the 2ed interface
	to_doc_a(file_name,int_two)
	big_line_two = """<y:LabelModel>
	          <y:SmartEdgeLabelModel autoRotationEnabled=\"false\" defaultAngle=\"0.0\" defaultDistance=\"10.0\"/>
	        </y:LabelModel>
	        <y:ModelParameter>
	          <y:SmartEdgeLabelModelParameter angle=\"0.0\" distance=\"30.0\" distanceToCenter=\"true\" position=\"right\" ratio=\"0.5\" segment=\"0\"/>
	        </y:ModelParameter>
	        <y:PreferredPlacementDescriptor angle=\"0.0\" angleOffsetOnRightSide=\"0\" angleReference=\"absolute\" angleRotationOnRightSide=\"co\" distance=\"-1.0\" frozen=\"true\" placement=\"anywhere\" side=\"anywhere\" sideReference=\"relative_to_edge_flow\"/>
	      </y:EdgeLabel>
	      <y:BendStyle smoothed=\"false\"/>
	    </y:PolyLineEdge>
	  </data>
	</edge>
	"""
	to_doc_a(file_name,big_line_two)
#XML to make the node (router/switch)
def make_node(ip):
	#print (ip)
	if ip not in nodes:
		nodes.append(ip)
		#print (ip)
		#Hard coded file name... BOOO!!
		to_doc_a(file_name,"<node id=\"")
		#IP address/node name
		to_doc_a(file_name,ip)
		big_line_three = """\">
		<data key=\"d5\"/>
		<data key=\"d6\">
			<y:ShapeNode>
			<y:Geometry height=\"30.0\" width=\"128.0\" x=\"686.0\" y=\"448.0\"/>
			<y:Fill color=\"#FFCC00\" transparent=\"false\"/>
			<y:BorderStyle color=\"#000000\" type=\"line\" width=\"1.0\"/>
			<y:NodeLabel alignment=\"center\" autoSizePolicy=\"content\" fontFamily=\"Dialog\" fontSize=\"12\" fontStyle=\"plain\" hasBackgroundColor=\"false\" hasLineColor=\"false\" height=\"18.701171875\" modelName=\"custom\" textColor=\"#000000\" visible=\"true\" width=\"10.673828125\" x=\"9.6630859375\" y=\"5.6494140625\">"""
		to_doc_a(file_name,big_line_three)
		#This is what will show up as a label for the node
		to_doc_a(file_name,ip)
		big_line_four ="""	            <y:LabelModel>
				<y:SmartNodeLabelModel distance=\"4.0\"/>
				</y:LabelModel>
				<y:ModelParameter>
				<y:SmartNodeLabelModelParameter labelRatioX=\"0.0\" labelRatioY=\"0.0\" nodeRatioX=\"0.0\" nodeRatioY=\"0.0\" offsetX=\"0.0\" offsetY=\"0.0\" upX=\"0.0\" upY=\"-1.0\"/>
				
				</y:ModelParameter>)
			</y:NodeLabel>
			<y:Shape type=\"rectangle\"/>
			</y:ShapeNode>
		</data>
		</node>
"""
		to_doc_a(file_name,big_line_four)
file_name = 'ugly.graphml'
to_doc_w(file_name, "")
to_doc_a(file_name,start)
read_node('results.csv')
read_in_conn('results.csv',connection)
to_doc_a(file_name,end)		
		
