import System.IO (readFile, writeFile)
import Data.List (replicate)


generateLine :: Int -> Int -> String
generateLine n i = replicate (n - i - 1) ' ' ++ replicate (2 * i + 1) '*'


generateDiamond :: Int -> [String]
generateDiamond n = upperHalf ++ lowerHalf
  where
    upperHalf = [generateLine n i | i <- [0..(n-1)]]
    lowerHalf = [generateLine n i | i <- [(n-2), (n-3)..0]]


main :: IO ()
main = do
    
    input <- readFile "input.txt"
    let n = read (head (lines input)) :: Int

  
    let diamond = unlines (generateDiamond n)


    writeFile "output.txt" diamond

    putStrLn "Diamond pattern written to output.txt"

