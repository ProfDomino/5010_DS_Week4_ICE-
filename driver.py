# add import here

def test_find(root, name, expectation_message):
    print(expectation_message)
    # test that BFS is working properly:
    n = root.bfs(name)
    if n is not None:
        print(str(n) +"'s direct reports are..." )
        if not n.is_leaf():
            for c in n.children:
                print("\t", c, end="")
        else: 
            print(n, "is a leaf node")
        print()
    else:
        print("failed to find", name)

def set_up_employee_tree():
    root = TreeNode("CEO")

    # CEO manages Tadashi
    root.add_employee_by_name("Tadashi", "CEO")
    # Tadashi manages Ewen
    root.add_employee_by_name("Ewen", "Tadashi")
    # Ewen manages Tyrone
    root.add_employee_by_name("Tyrone", "Ewen")

    # CEO manages Senka
    root.add_employee_by_name("Senka", "CEO")

    # Senka manages Amy and Abdul
    root.add_employee_by_name("Amy", "Senka")
    root.add_employee_by_name("Abdul", "Senka")

    # Amy manages Jeff, Argos, and Tama
    root.add_employee_by_name("Jeff", "Amy")
    root.add_employee_by_name("Argos", "Amy")
    root.add_employee_by_name("Tama", "Amy")
    return root

def main():
    root = set_up_employee_tree()
    can_find1 = "Amy"
    expectation1= str("Looking for, "+ can_find1+ " should print "+ can_find1+ " and their 3 direct reports")
    test_find(root, can_find1, expectation1)
    print("-----")
    can_find2 = "Tyrone"
    expectation2 = str("Looking for, "+ can_find2+ " should print "+ can_find2+ " and their 0 direct reports")
    test_find(root, can_find2, expectation2)
    print("-----")
    cant_find = "Thalia"
    expectation3 = str("Looking for, "+ cant_find + " should fail to find")
    test_find(root, cant_find, expectation3)

if __name__ == "__main__":
    main()
