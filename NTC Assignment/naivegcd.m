function gcd = naivegcd(a, b)
  gcd = -1;                                    %if invalid inputs (-ve numbers) then return -1
  if (a >= 0) && (b >= 0) && (a + b) > 0       %checking validity of inputs
  	if a == 0 || b == 0
        gcd = max_u(a,b);                        %checking if one input is 0 return the other
        return
    end
  	for d = min_u(a,b):-1:0                      %iterating from the min of a,b till it reaches 0
  		if (mod_u(a,d) == 0) && (mod_u(b,d) == 0)  %checking if we get a divisor that divides both a,b
            gcd = d;
  			return;
        end
    end
    gcd = 1;                                   %if no such divisor exists return gcd as 1
  	return
  end
return;
end




% The following call would take too long
%print(gcd(790933790547, 1849639579327))