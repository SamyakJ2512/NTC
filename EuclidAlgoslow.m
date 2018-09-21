function gcd = EuclidAlgoslow (a, b)
  if a >= 0 && b >= 0 && a + b > 0

  while a > 0 && b > 0
    if a >= b
      a = a - b;
    else
      b = b - a;
    end
  end
  gcd = max(a,b);
  return;
  end
  gcd = -1;
  return;
end
   