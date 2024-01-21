{-# LANGUAGE OverloadedStrings #-}

import System.Environment
import System.IO
import Data.Aeson (Value, encode, decode)
import qualified Data.ByteString.Lazy as BS

recvRequest :: IO (Maybe Value)
recvRequest = do
  args <- getArgs
  let n = read (last args) :: Int
      filePath = "." ++ show n ++ ".input"
  contents <- tryReadFile filePath
  case contents of
    Just data' -> return (decode data')
    Nothing -> do
      hPutStrLn stderr "Error reading input file"
      return Nothing

sendResponse :: Value -> IO ()
sendResponse response = do
  args <- getArgs
  let n = read (last args) :: Int
      filePath = "." ++ show n ++ ".output"
  success <- tryWriteFile filePath (encode response)
  unless success $ hPutStrLn stderr "Error writing output file"

tryReadFile :: FilePath -> IO (Maybe BS.ByteString)
tryReadFile path = do
  result <- try $ BS.readFile path
  case result of
    Left (_ :: IOException) -> return Nothing
    Right contents -> return (Just contents)

tryWriteFile :: FilePath -> BS.ByteString -> IO Bool
tryWriteFile path contents = do
  result <- try $ BS.writeFile path contents
  return $ case result of
    Left (_ :: IOException) -> False
    Right _ -> True