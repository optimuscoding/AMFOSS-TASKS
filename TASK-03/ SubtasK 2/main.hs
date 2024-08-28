import System.IO (readFile, writeFile)

main :: IO ()
main = do
    let inputFilePath = "input.txt"
    let outputFilePath = "output.txt"

 
    content <- readFile inputFilePath
    
    writeFile outputFilePath content

    putStrLn $ "Content successfully copied from " ++ inputFilePath ++ " to " ++ outputFilePath
