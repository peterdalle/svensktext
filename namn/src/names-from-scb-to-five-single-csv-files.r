library(rio)

load_process_and_save <- function(infile, outfile, sheet) {
  df <- rio::import(infile, sheet=sheet, skip=3)
  colnames(df) <- c("name", "persons")
  write.csv(df, file=outfile, fileEncoding="UTF-8", quote=FALSE, row.names=FALSE)
}

# efternamn
load_process_and_save(infile = "namn-med-minst-tva-barare-31-december-2020.xlsx", 
                      outfile = "efternamn.csv",
                      sheet = 1)

# förnamn kvinnor
load_process_and_save(infile = "namn-med-minst-tva-barare-31-december-2020.xlsx", 
                      outfile = "fornamn-kvinnor.csv",
                      sheet = 2)

# förnamn män
load_process_and_save(infile = "namn-med-minst-tva-barare-31-december-2020.xlsx", 
                      outfile = "fornamn-man.csv",
                      sheet = 3)

# tilltalsnamn kvinnor
load_process_and_save(infile = "namn-med-minst-tva-barare-31-december-2020.xlsx", 
                      outfile = "tilltalsnamn-kvinnor.csv",
                      sheet = 4)

# tilltalsnamn män
load_process_and_save(infile = "namn-med-minst-tva-barare-31-december-2020.xlsx", 
                      outfile = "tilltalsnamn-man.csv",
                      sheet = 5)
