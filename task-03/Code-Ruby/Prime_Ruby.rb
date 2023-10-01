def is_prime(n)
  return false if n <= 1

  (2..Math.sqrt(n)).each do |i|
    return false if n % i == 0
  end

  true
end

def prime_numbers(n)
  (2..n).each do |i|
    puts i if is_prime(i)
  end
end

print "Enter the No upto which to print Prime Number:"
n = gets.chomp.to_i
prime_numbers(n)

