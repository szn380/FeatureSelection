
# Overview
#   1) generate/input list of features
#   2) create list of possible products based on combinations of features
#   3) identify non dominated set of products

partList = {"Part1": 5, "Part2": 4, "Part3": 6}

print("Part List:")
print("Name \tCost")
for element in partList:
	print("{0} \t{1}".format(element, partList[element]))
print("\n")

# here is where the feature list is created
featList = [['ForColAlert', 3.0, 0.6, 0, ["Part1"]], ['SideBlindZone', 2.0, 0.5, 0, ["Part1", "Part2"]], ['LaneKeeping', 3.0, 0.4, 0, ["Part3"]]]

FNAME = 0  # Feature name
FCOST = 1  # Feature cost
FVAL = 2   # Feature value
FINCR = 3  # value of 0 1, used for counting up to
           # decide if a feature is in a product or not
           # 0 = feature is not in product; 1 = feature is in
FPARTS = 4 # parts list for feature

PNUM = 0        # Product number (for reference)
PCOST = 1       # Product cost     
PVAL = 2        # Product value
PFEATLIST = 3   # list of features that are included in the product
PPARTLIST = 4   # list of parts needed for the features in the product

featListLen = len(featList)
prodListSize = 2 ** featListLen

# print feature list
print("Feature List:")
print("Name \t\tValue\tParts")
for i in featList:
    print("{0} \t{1}\t".format(i[FNAME], i[FVAL]), end='')
    for j in i[FPARTS]:
        print("{}\t".format(j), end='')
    print()

print("\n")

# print out product list during construction of product list
print("Product List:")
print("Num. \tCost\tValue\tFeatures")
productList = []

# build up product list by looking at all combinations of features
#    basically counting up 000, 001, 010, ...    where FINCR of feature is its "bit"
#    to generate all possible products
for i in range(0, prodListSize):
    cost = 0
    value = 0

    # determine new product cost and value
    for j in range(0, featListLen):
        if featList[j][FINCR] == 1:
            # cost += featList[j][FCOST]
            value += featList[j][FVAL]
            # determine product cost
            # for k in featList[j][FPARTS]
                    
    
    #print out new product
    print("{0} \t{1} \t{2} \t".format(i,cost,value), end='')
 
    featureList = list()
    for j in range(0, featListLen):
        if featList[j][FINCR] == 1:
            print("{} ".format(featList[j][FNAME]), end='')
            featureList.append(featList[j][FNAME])
    print()
    productList.append([i, cost, value, featureList, []])

    # generate next product
    carry = 1
    for j in range(0, featListLen):
        if (featList[j][FINCR] == 0) and (carry == 1):
            featList[j][FINCR] = 1
            carry = 0
        elif (featList[j][FINCR] == 1) and (carry == 1):
            featList[j][FINCR] = 0
            carry = 1
print()

    
# determine non dominated products
#    original product list is "productList"
#    non dominated products are saved / moved to "productList"
productList1 = []
done = 0
while done==0:
    loopSize = len(productList)
    if loopSize > 0:
        notDominated = 1
        repeatLoop  = 0
        # compare first element in productList to all others
        # if first element is dominated, remove it
        # if first element dominates another, remove the other element
        # loop starts over each time after an element is removed so that the for loop indice does not get messed up
        for i in range(1,loopSize):
            # is first element dominated
            if (productList[0][PCOST] >= productList[i][PCOST]) and (productList[0][PVAL] < productList[i][PVAL]):
                notDominated = 0
                del productList[0]
                repeatLoop = 1
                break
            if (productList[0][PCOST] > productList[i][PCOST]) and (productList[0][PVAL] <= productList[i][PVAL]):
                notDominated = 0
                del productList[0]
                repeatLoop = 1
                break
            # does first element dominate another element in the list
            if (productList[0][PCOST] <= productList[i][PCOST]) and (productList[0][PVAL] > productList[i][PVAL]):
                del productList[i]
                repeatLoop = 1
                break
            if (productList[0][PCOST] < productList[i][PCOST]) and (productList[0][PVAL] >= productList[i][PVAL]):
                del productList[i]
                repeatLoop = 1
                break
        # transfer first element to output list if it is not dominated the the search (for) loop fully completed
        if notDominated and repeatLoop == 0:
            saveProduct = productList[0].copy()
            productList1.append(saveProduct)
            del productList[0]            
    else:
        done = 1
        
# print out list of non dominated products
print("\n\nNon-Dominated Product List:")
print("Num. \tCost\tValue\tFeatures")
loopSize = len(productList1)
for i in range(0, loopSize):
    print("{0} \t{1} \t {2}\t ".format(productList1[i][PNUM], productList1[i][PCOST], productList1[i][PVAL]), end='')
    numFeatures = len(productList1[i][PFEATLIST])
    temp = productList1[i][PFEATLIST].copy()
    for j in range(0, len(temp)):
        print("{}\t".format(temp[j]), end='')
    print()

              
        
        

    

    
