from dumper import Dump
import argparse

def parse_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-all", \
                        action='store_true', \
                        help="Dump all the tables")
    parser.add_argument("-tbl", \
                        help="TABLE_NAME to dump the columns, default table is 'mahasiswa'")
    parser.add_argument("-col", \
                        help="Number of columns you want to dump")
    parser.add_argument("--data", \
                        help="Dump data from specific column of a table")
    parser.add_argument("--order", \
                        help="Order by specific column")
    parser.add_argument("--outfile", \
                        help="OUTPUT file for the dumped things")

    return parser.parse_args()

def main():
    args = parse_argument()
    url = "http://repository.undiknas.ac.id/repository/search"
    data = Dump(url)
    if args.all:
        data.dumpTable()
    if args.tbl and args.col and args.data:
        if args.order:
            if args.outfile:
                return data.dumpData(table=args.tbl,columns=int(args.col), save_file=args.outfile, column_name=args.data, order=args.order)
            else:
                return data.dumpData(table=args.tbl, columns=int(args.col), column_name=args.data, order=args.order)
        else:
            if args.outfile:
                return data.dumpData(table=args.tbl, columns=int(args.col), save_file=args.outfile, column_name=args.data)
            else:
                return data.dumpData(table=args.tbl, columns=int(args.col), column_name=args.data)
    elif args.tbl and args.col:
        if args.outfile:
            return data.dumpColumns(table=args.tbl, save_file=args.outfile, columns=args.col)
        else:
            return data.dumpColumns(table=args.tbl, columns=int(args.col))
    elif args.tbl:
        if args.outfile:
            return data.dumpColumns(table=args.tbl,save_file=args.outfile)
        else:
            print "Output in the default file: outputcol.txt"
            return data.dumpColumns(table=args.tbl)
    else:
        return print "Please fill the data"

if __name__ == "__main__":
    main()