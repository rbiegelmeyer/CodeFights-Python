def countSumOfTwoRepresentations2(n, l, r):
    cont  = 0;
    for a in range(r):
      b = n - a
      if (b >=l and b<=r and b >=a):
        cont += 1

    return cont