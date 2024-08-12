def adjust_results4_isadog(results_dic, dogfile):
               
    dognames_dic = dict()

    with open (dogfile,"r") as df:
      rd_line = df.readline()

      while rd_line != "":
        rd_line = rd_line.lower().strip()

        if rd_line not in dognames_dic:
          dognames_dic[rd_line] = 1
        else:
          dognames_dic[rd_line] = 0

        rd_line = df.readline()

      for key in results_dic:
         if results_dic[key][0] in dognames_dic:
            if results_dic[key][1] in dognames_dic:
              results_dic[key].extend((1, 1))
            else:
              results_dic[key].extend((1, 0))
            
         else:
          if results_dic[key][1] in dognames_dic:
            results_dic[key].extend((0, 1))
          else:
            results_dic[key].extend((0, 0))


