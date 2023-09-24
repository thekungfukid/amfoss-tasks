defmodule PrimeNumbers do
  def is_prime(n) when n <= 1, do: false
  def is_prime(n) do
    Enum.all?(2..round(:math.sqrt(n)), fn i -> rem(n, i) != 0 end)
  end

  def prime_numbers(n) do
    Enum.each(2..n, fn i -> if is_prime(i), do: IO.write("#{i} ") end)
    IO.puts()
  end
end

IO.puts("Enter the number up to which to print Prime Numbers:")
n = IO.gets("") |> String.trim() |> String.to_integer()

PrimeNumbers.prime_numbers(n)

