import Data.Char (ord)
import System.IO

-- Function to split a string by comma without external libraries
splitByComma :: String -> [String]
splitByComma = go ""
  where
    go :: String -> String -> [String]
    go acc []       = [reverse acc]
    go acc (',':xs) = reverse acc : go "" xs
    go acc (x:xs)   = go (x:acc) xs

-- Turn string into int array
parseInts :: String -> [Int]
parseInts str = map read (words str)

-- Get the hash value of a given string
getHash :: [Char] -> Int
getHash [] = 0
getHash (x:xs) = (getHash xs + ord x) * 17 `mod` 256

main = do
    -- -- read just a line and convert to a list of Ints
    -- inputString <- fmap parseInts getLine
    
    handle <- openFile "input.txt" ReadMode
    contents <- hGetContents handle

    let inputString = contents
    let inputValues = splitByComma inputString

    let hashes = map getHash $ map reverse inputValues

    let sumPt1 = sum hashes
    print sumPt1