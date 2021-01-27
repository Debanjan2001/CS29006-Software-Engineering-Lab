import java.util.*;

public class Social {
		
	public ArrayList<node> nodesList;
	public ArrayList<post> allPosts;
	public int idGenerator;

	public Social()
	{
		this.nodesList =  new ArrayList<node>();
		this.idGenerator = 1;
		this.allPosts = new ArrayList<post>();
	}
	
	public void features() {
		
		System.out.println("Enter 1 to create a node");
		System.out.println("Enter 2 to delete a node");
		System.out.println("Enter 3 to search for a node");
		System.out.println("Enter 4 to see all linked nodes of an input node");
		System.out.println("Enter 5 to create and post some content for some user");
		System.out.println("Enter 6 to search for content posted by any node");
		System.out.println("Enter 7 to display all contents posted by nodes linked to a given node");
		System.out.println("Enter 8 to print all nodes");
		System.out.println("Enter 9 to create links between nodes");
		System.out.println("Enter -1 to exit the program");
		System.out.print("\n");

	}
	
	public void createNode(Scanner sc) {
		
		System.out.println("Enter type of node:");
		
		String nodeType = sc.nextLine();
		
		node newNode = null;
		
		if( nodeType.equals("individual") )
		{
			newNode = new individual(sc);
		}
		else if( nodeType.equals("group") )
		{
			newNode = new group(sc);

		}
		else if( nodeType.equals("business") )
		{
			newNode = new business(sc);
		}
		else if( nodeType.equals("organisation") )
		{
			newNode = new organisation(sc);
		}
		else
		{
			System.out.println("Enter a correct type of node");
		}

		if(newNode!=null)
		{
			newNode.id = idGenerator;
			idGenerator++;
			newNode.type = nodeType;
			nodesList.add(newNode);
			System.out.println("Successfully created a new node \n");	
		}
		
	}
	
	public void deleteNode(Social network,Scanner sc){
		
		System.out.println("Here are all the nodes:");
		network.printAllNodes();

		System.out.println("Enter the id of the node you want to delete");
		int id = sc.nextInt();
		sc.nextLine();

		for(int i=0;i<nodesList.size();i++)
		{
			if(nodesList.get(i).id == id )
			{
				for(node friend : nodesList.get(i).connections)
				{
					for(int j=0;j<friend.connections.size();j++)
					{
						if(friend.connections.get(j).id == id)
						{
							friend.connections.remove(j);
							break;
						}
					}
				}
				nodesList.remove(i);
				System.out.println("Successfully deleted the node \n");	
				return;
			}
		}

	}
	
	public void searchNode(Scanner sc) {
		
		System.out.println("You have 3 choices: \n Enter 1 to search using name \n Enter 2 to search using type \n Enter 3 to search using birthday");

		int query = sc.nextInt();
		sc.nextLine();

		System.out.println("Enter your text:");
		String pattern = sc.nextLine();

		ArrayList<node> querySet = new ArrayList<node>();

		for(int i=0;i<nodesList.size();i++)
		{
			if(query == 1)
			{
				if(nodesList.get(i).name.equals(pattern)  )
				{
					querySet.add(nodesList.get(i));
				}
			}
			else if(query == 2)
			{
				if(nodesList.get(i).type.equals(pattern)  )
				{
					querySet.add(nodesList.get(i));
				}
			}
			else if(query == 3 && nodesList.get(i).type.equals("individual") )
			{
				individual curr =  ((individual) nodesList.get(i));
				if( curr.birthday.equals(pattern) )
				{
					querySet.add(nodesList.get(i));
				}
			}
		
		}

		System.out.println("There are "+querySet.size() +" nodes found based on your search criteria");
		
		for(node n:querySet)
			System.out.println( n );
	}

	public void printLinkedNodes(Social network,Scanner sc) {

		System.out.println("Here are all the nodes:");
		network.printAllNodes();
		System.out.println("Enter id of the user for whom you want to see linked nodes");
		int id = sc.nextInt();
		sc.nextLine();

		for(node user : nodesList )
		{
			if(user.id == id)
			{
				if(user.type.equals("business"))
				{
					((business) user).printLinkedNodes();
				}
				else if(user.type.equals("group"))
				{
					((group) user).printLinkedNodes();
				}
				else if(user.type.equals("organisation"))
				{
					((organisation) user).printLinkedNodes();
				}
				else
				{
					((individual) user).printLinkedNodes();
				}
				return;
			}
		}
	}

	public void createContent(Social network,Scanner sc) {

		System.out.println("Here are all the nodes:");
		network.printAllNodes();
		System.out.println("Enter id of the user for whom you want to create content");
		int id = sc.nextInt();
		sc.nextLine();

		System.out.println("Do you want to repost some content? Enter y/n:");
		String choice = sc.nextLine();

		if(choice.equals("y"))
		{
			System.out.println("Enter id of the user whose content you want to repost");
			int secondId = sc.nextInt();
			sc.nextLine();

			for(node n:nodesList)
			{
				if(n.id == secondId)
				{
					for(int i=0;i<n.contents.size();i++)
					{
						System.out.println( (i+1)+ ". "+n.contents.get(i));
					}

					if(n.contents.size()==0)
					{
						System.out.println("No posts available for repost");
						break;
					}

					System.out.println("Enter Serial number of the content that you want to repost:");
					int serial = sc.nextInt();
					sc.nextLine();

					for(node user:nodesList)
					{
						if( user.id == id)
						{
							post content = n.contents.get(serial-1);
							user.contents.add(content);
							System.out.println("Successfully reposted");
							return;
						}
					}
				}
			}
		}
		else
		{
			System.out.println("ok...Enter the content:");
			String s = sc.nextLine();

			post content = new post(s);
			allPosts.add(content);

			for(node user : nodesList )
			{
				if(user.id == id)
				{
					user.createContent(content);
					return;
				}
			}

		}
	}

	public void searchContent(Social network,Scanner sc) {

		System.out.println("Here are all the nodes:");
		network.printAllNodes();
		System.out.println("Enter the id of the user whose contents you want to search :");
		int id = sc.nextInt();
		sc.nextLine();

		for(node user : nodesList)
		{
			if(user.id == id)
			{
				for(post content: user.contents)
				{
					System.out.println(content);
				}
				return;
			}
		}
	}
	
	public void displayLinkedContent(Social network,Scanner sc) {
		
		System.out.println("Here are all the nodes:");
		network.printAllNodes();
		System.out.println("Enter id of the user for whom you want to see posts by his/her linked nodes ");
		int id = sc.nextInt();
		sc.nextLine();

		for(int i=0;i<nodesList.size();i++)
		{
			if(nodesList.get(i).id == id)
			{
				for(node friend : nodesList.get(i).connections)
				{
					if(friend.contents.size()>0)
						System.out.println("Posts by "+friend.name);
					for(post content : friend.contents )
					{
						System.out.println(content);
					}
				}
				return;
			}
		}
	}
	
	public void printAllNodes() {
		
		for (int i = 0; i < nodesList.size(); i++) {
			System.out.println( (i+1)+" ) "+ nodesList.get(i) );
		}
		
	}
	
	public void createLink(Social network,Scanner sc)
	{
		System.out.println("Here are all the nodes:");
		network.printAllNodes();
		System.out.println("Enter id of the node from which you want to create a link");
		int from = sc.nextInt();
		sc.nextLine();
		System.out.println("Enter id of the node to which you want to create a link");
		int to = sc.nextInt();
		sc.nextLine();

		node u = null,v = null;
		for(node n:nodesList){
			if(n.id == from)
			{
				u = n;
			}
			if(n.id == to)
			{
				v = n; 
			}
		}

		int ok = 0; //Successful connection checker
		if(u.type.equals("business"))
		{
			if(v.type.equals("individual"))
			{
				ok=1;
				u.connections.add(v);
				v.connections.add(u);

				System.out.println("Is "+v.name + " owner of "+u.name+"?Enter y/n:");
				String choice = sc.nextLine();
				business curr = ( (business) u);
				if(choice.equals("y") )
				{
					curr.owners.add(v);
				}
				
				System.out.println("Is "+v.name + " customer ofof "+u.name+"?Enter y/n:");
				choice = sc.nextLine();
				if(choice.equals("y") )
				{
					curr.customers.add(v);
				}
				
			}
			else if(v.type.equals("group"))
			{
				ok = 1;
				u.connections.add(v);
				v.connections.add(u);
			}
		}
		else if(u.type.equals("organisation"))
		{
			if(v.type.equals("individual"))
			{
				ok=1;
				u.connections.add(v);
				v.connections.add(u);

				System.out.println("Is "+v.name+" a member of "+u.name+ "?Enter y/n:");
				String choice = sc.nextLine();

				if(choice.equals("y"))
				{
					((organisation)u).members.add(v);
				}
			}
		}
		else if(u.type.equals("group") )
		{
			if(v.type.equals("individual") || v.type.equals("business"))
			{
				ok = 1;
				u.connections.add(v);
				v.connections.add(u);

				System.out.println("Is "+v.name+" a member of "+u.name+ "?Enter y/n:");
				String choice = sc.nextLine();

				if(choice.equals("y"))
				{
					((group)u).members.add(v);
				}

			}
		}
		else if(u.type.equals("individual") )
		{
			ok = 1 ;
			if(v.type.equals("business"))
			{
				System.out.println("Is "+u.name + " owner of "+v.name+"?Enter y/n:");
				String choice = sc.nextLine();
				business curr = ( (business) v);
				if(choice.equals("y") )
				{
					curr.owners.add(u);
				}

				System.out.println("Is "+u.name + " customer of "+v.name+"?Enter y/n:");
				choice = sc.nextLine();

				if(choice.equals("y") )
				{
					curr.customers.add(u);
				}
			}
			else if( v.type.equals("group") || v.type.equals("organisation"))
			{
				System.out.println("Is "+u.name + " member of "+ v.name +"?Enter y/n:");
				String choice = sc.nextLine();
				if(choice.equals("y") )
				{
					if(v.type.equals("group"))
					{
						( (group) v ).members.add(u);
					}
					else
					{
						( (organisation) v ).members.add(u);
						
					}
				}
			}

			if(u.id != v.id)
			{
				u.connections.add(v);
				v.connections.add(u);
			}
			else
				ok = 0;
			
		}

		if(ok==0)
		{
			System.out.println("This type of connection is not possible");
		}
		else
		{
			System.out.println("Successfully linked!");
		}
	}

	public static void main(String args[]) {
		System.out.println("Welcome to social network...");
		
		Scanner sc = new Scanner(System.in);
		
		int input = 0;
		
		Social network = new Social();
		
		while(input!=-1) {
			
			network.features();

			input = sc.nextInt();
			sc.nextLine();
			
			if(input == 1)
			{
				network.createNode(sc);
			}
			else if(input == 2)
			{
				network.deleteNode(network,sc);
			}
			else if(input == 3)
			{
				network.searchNode(sc);
			}
			else if(input == 4)
			{
				network.printLinkedNodes(network,sc);
			}
			else if(input == 5)
			{
				network.createContent(network,sc);
			}
			else if(input == 6)
			{
				network.searchContent(network,sc);
			}
			else if(input == 7)
			{
				network.displayLinkedContent(network,sc);
			}
			else if(input == 8)
			{
				network.printAllNodes();
			}
			else if(input == 9)
			{
				network.createLink(network,sc);
			}
			else if(input != -1)
			{
				System.out.println("Check your choice again");
			}

			System.out.print("\n");
			
		}
	}
}

class node {
	
	public String type,name,creationDate;
	public int id;
	public ArrayList<post> contents;
	public ArrayList<node> connections;

	public node(Scanner sc){
		
		System.out.println("Enter name: ");
		this.name = sc.nextLine();
		this.creationDate = new Date().toString();
		this.contents =  new ArrayList<post>();
		this.connections = new ArrayList<node>();
	}
	
	public void createContent(post s) 
	{
		contents.add(s);
		System.out.println("Succesfully posted!");
	}	

	public String toString()
	{
		return "Name: "+name +" ,Account type: "+type+" ,id: "+id +",Profile created on: "+creationDate;  
	}
}


class individual extends node {
	
	public String birthday;
	
	public individual(Scanner sc) {
		super(sc);
		
		System.out.println("Enter birthday:");
		this.birthday = sc.nextLine();
	} 

	public void printLinkedNodes()
	{
		for(node n:super.connections)
		{
			System.out.println(n);
		}
	}
	
}

class business extends node {

	public int locX,locY;
	public HashSet<node> owners,customers; 
	
	public business(Scanner sc) {
		
		super(sc);
		System.out.println("Enter X-corodinate and Y-co-ordinate using one space");
		this.locX = sc.nextInt();
		this.locY = sc.nextInt();
		sc.nextLine();

		this.owners =  new HashSet<node>();
		this.customers =  new HashSet<node>();
	}		

	public void printLinkedNodes()
	{
		for(node n:super.connections)
		{
			if(owners.contains(n))
			{
				System.out.print("OWNER: ");
			}
			else if(customers.contains(n))
			{
				System.out.print("CUSTOMER: ");
			}
			System.out.println(n);
		}
	}
}

class organisation extends node {
	
	public int locX,locY;
	public HashSet<node> members;
	
	public organisation(Scanner sc) {
		super(sc);

		this.members = new HashSet<node>();

		System.out.println("Enter X-corodinate and Y-co-ordinate using one space");
		this.locX = sc.nextInt();
		this.locY = sc.nextInt();
		sc.nextLine();
		
	}	

	public void printLinkedNodes()
	{
		for(node n:super.connections)
		{
			if(members.contains(n))
			{
				System.out.print("MEMBER: ");
			}
			System.out.println(n);

		}
	}

}

class group extends node {

	public HashSet<node> members;

	public group(Scanner sc) {
		super(sc);
		this.members = new HashSet<node>();
	}

	public void printLinkedNodes()
	{
		for(node n:super.connections)
		{
			if(members.contains(n))
			{
				System.out.print("MEMBER: ");
			}
			System.out.println(n);

		}
	}
	
}

class post{

	public String content;
	
    public post(String s)
    {
        this.content = s;
    }

    public String toString(){
        return this.content;
    }
}

