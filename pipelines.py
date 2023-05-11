# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
import os

class BookPipeline(object):
      def open_spider(self,spider):
            print("open_spider")
            self.con=sqlite3.connect("books.db")
            self.cursor=self.con.cursor()
            try:
                  self.cursor.execute("drop table books")
            except:
                  pass
            sql="create table books (ID varchar(8) primary key,bTitle varchar(256),bAuthor varchar(256),bPublisher varchar(256),bDate varchar(256),bPrice varchar(256),bDetail text,bImage varchar(256))"
            self.cursor.execute(sql)
            if not os.path.exists("download"):
                  os.mkdir("download")

      def close_spider(self,spider):
            print("close_spider")
            print("Total ",spider.count)
            self.con.commit()
            self.con.close()

      def insertDB(self,ID,bTitle,bAuthor,bPublisher,bDate,bPrice,bDetail,bImage):
            try:
                  sql="insert into books (ID,bTitle,bAuthor,bPublisher,bDate,bPrice,bDetail,bImage) values (?,?,?,?,?,?,?,?)"
                  self.cursor.execute(sql,[ID,bTitle,bAuthor,bPublisher,bDate,bPrice,bDetail,bImage])
            except Exception as err:
                  print(err)

      def process_item(self, item, spider):
            ID=item["ID"]
            bTitle=item["bTitle"]
            bAuthor=item["bAuthor"]
            bPublisher=item["bPublisher"]
            bDate=item["bDate"]
            bPrice=item["bPrice"]
            bDetail=item["bDetail"]
            bImage=item["bImage"]
            print(ID,bTitle)
            self.insertDB(ID,bTitle,bAuthor,bPublisher,bDate,bPrice,bDetail,bImage)
            return item
