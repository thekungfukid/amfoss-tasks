import System.IO

isPrime :: Int -> Bool
isPrime n
    | n <= 1 = False
    | otherwise = all (\i -> n `mod` i /= 0) [2..intSqrt n]
    where intSqrt = floor . sqrt . fromIntegral

primeNumbers :: Int -> [Int]
primeNumbers n = [x | x <- [2..n], isPrime x]

main :: IO ()
main = do
    putStr "Enter the No upto which to print Prime Number:"
    hFlush stdout
    input <- getLine
    let n = read input :: Int
    let primes = primeNumbers n
    putStrLn $ unwords $ map show primes

