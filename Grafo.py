#TAD DE GRAFOS
#El grafo en python se representa en diccionario
class Graph(object):
    def __ini__(self,graph_dict=None):
        if graph_dict==None:
            #CREO UN DICCIONARIO VACIO
            graph_dict={}
            #SI NO ESTA VACIO DEVUELVE EL GRAFO
            self._graph_dict=graph_dict

    """se retorna en las dos siguientes funciones los vertices y las aristas"""
    def vertices(self):
        return list(self._graph_dict.keys())

    def edges(self):
        return self._generate_edges()

    def add_vertex(self,vertex):
        if vertex not in self._graph_dict:
            self._graph_dict[vertex]=[]
    def add_edges(self,edges):
        edge=set(edge)
        (vertex1,vertex2)=tuple(edge)
        if vertex1 in self._graph_dict:
            self._graph_dict[vertex1].append(vertex2)
        else:
            self._graph_dict[vertex1]=[vertex2]
  
    def _generate_edges(self):
        edge=[]
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if{neighbour,vertex} not in edges:
                    edges.append({vertex,neighbour})
        return edges
    def __str__(self):
        res="vertices:"
        for k in self._graph_dict:
            res=str(k)+ ""
        res+= "\n edges: "
        for edge in self._generate_edges():
            res+=str(edges)+""
        return res


if __name__ == "__main__":
	#---------------------------------Implementación de funciones básicas---------------------------------#
	# Creo el grafo con un diccionario
	# Lo que esta a la derecha de los ':' son los vértices
	# Lo que esta a la izquierda de los ':' entre '[]' son las listas de adyacencias de esos vértices
	g={	'a' : ['d'],
		'b' : ['c'],
		'c' : ['b','c','d','e'], # 'c' tiene un ciclo porque se repite en su lista de adyacencia
		'd' : ['a','c'],
		'e' : ['c'],
		'f' : [] # 'f' es un vértice aislado porque no tiene nada en su lista de adyacencia
	}

	"""# Instancio el objeto pasandole como parámetro el grafo que cree anteriormente
	print("Implementación de funciones básicas:")
	graph = Graph(g)
	print("1) Vertices del grafo: ")
	print(graph.vertices()) # Imprimo los vertices
	print("2) Aristas del grafo: ")
	print(graph.edges()) # Imprimo las aristas
	print("3) Agrego un vertice 'z': ")
	graph.add_vertex("z")
	print("- Vertices del grafo: ")
	print(graph.vertices())
	print("4) Agrego una arista {'a','z'}: ")
	graph.add_edge({"a","z"})
	print("- Aristas del grafo: ")
	print(graph.edges())
	# Ahora intento agregar aristas con vértices que no existen
	print("5) Agregando una arista {'x','y'} con nuevos vertices: ")
	graph.add_edge({"x","y"})
	print("- Vertices: ")
	print(graph.vertices())
	print("- Aristas: ")
	print(graph.edges())
	print("------------------------------------------------------------------------------------")
	"""

        
    
    
