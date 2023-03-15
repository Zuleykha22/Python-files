// Write the following code in Javascript:

// def countZeroRowsAndColumns(list1, list2):
//   res = [lst1[0][i] + lst2[0][i] for i in range(3)]
//   res_two = [lst1[1][i] + lst2[1][i] for i in range(3)]
//   counter = 0
//   if all(res) == False:
//     counter += 1
//   elif all(res_two) == False:
//     counter += 1
//   for i in range(3):
//     if res[i] == 0 and res_two[i] == 0:
//       counter += 1
//   return counter 


// function countZeroRowsAndColumns(list1, list2){
//   res = [lst1[0][i] + lst2[0][i] for i in range(3)]
//   res_two = [lst1[1][i] + lst2[1][i] for i in range(3)]
//   counter = 0
//   if all(res) == False:
//     counter += 1
//   else if all(res_two) == False:
//     counter += 1
//   for i in range(3):
//     if res[i] == 0 and res_two[i] == 0:
//       counter += 1
//   return counter 
// }