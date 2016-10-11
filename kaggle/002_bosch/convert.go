package main

import (
  "fmt"
  "os"
  "time"
  "strconv"
  "strings"
  "encoding/csv"
)

var list []string = []string{"", "T-2147482688", "T16384", "T589824", "T748928", "T8651776", "T145", "T786944", "T64", "T16777232", "T256", "T83888", "T143", "T6553", "T2516", "T16777472", "T16777216", "T8389632", "T9174", "T12582912", "T86752", "T514", "T492", "T63616", "T56", "T16777248", "T41944", "T113776", "T-2147482176", "T4", "T128", "T134217728", "T917", "T18436", "T96112", "T786432", "T1152", "T678864", "T32896", "T9", "T524544", "T1", "T7", "T1132", "T65536", "T16", "T32", "T52", "T-2147482432", "T25165824", "T16777557", "T91764", "T-2147482816", "T36992", "T6", "T96", "T-21474872", "T33554944", "T8768", "T4718592", "T5", "T98", "T-2147483648", "T-21474825", "T33554432", "T-18748192", "T2", "T48576", "T16779428", "T11141888", "T55424", "T-2147482944", "T618624", "T512", "T178258", "T1310", "T3", "T-2147481664", "T8912896", "T33554448", "T-2147483647", "T8", "T26808", "T-21474819", "T262144", "T48", "T331648", "T524288", "T1372", "T24", "T-2147483646", "T16512", "T268435456", "T97"}

func main() {
  d := map[string]string{}
  for i, v := range list {
    d[v] = strconv.FormatInt(int64(i), 10)
  }
  fmt.Println(list, d)
  f, err := os.Open("test_categorical.csv")
  if err != nil {
    fmt.Println(err)
    os.Exit(1)
  }

  file, err := os.OpenFile("test_categorical_c.csv", os.O_RDWR|os.O_CREATE|os.O_SYNC|os.O_TRUNC, 0775)
  if err != nil {
    fmt.Println(err)
    os.Exit(1)
	}
  w := csv.NewWriter(file)

  defer f.Close()
  defer file.Close()
  lines := csv.NewReader(f)

  i := -1
  for {
    i++
    row, err := lines.Read()
    if err != nil {
      fmt.Println(err)
      break
    }
    for i, v := range row {
      if r, ok := d[v]; ok {
        row[i] = r
      }
    }

    if err = w.Write(row); err != nil {
			fmt.Println("error writing record to csv:", err)
		}
    if len(row) != 2141{
      fmt.Println(i, row[0],len(row), "wrong len", row)
    }
    if row[0] == "2367495" || row[0] == "2367494" {
      fmt.Println(strings.Join(row, ","))
    }
    //fmt.Printf("%d, %+v\n", len(row), row)
    if i % 1000 == 0 {
      fmt.Println(i)
    }
  }
  time.Sleep(time.Second)

}
