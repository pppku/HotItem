package com.jimmyli.hotitems_analysis

import java.util.Properties

import org.apache.kafka.clients.producer.{KafkaProducer, ProducerRecord}

object KafkaProducer {
  def main(args: Array[String]): Unit = {
    writeToKafka("hotitems")
  }
  def writeToKafka(topic: String): Unit ={
    val properties = new Properties()
    properties.put("bootstrap.servers", "172.16.159.146:9092")
    properties.setProperty("key.serializer", "org.apache.kafka.common.serialization.StringSerializer")
    properties.setProperty("value.serializer", "org.apache.kafka.common.serialization.StringSerializer")

    // 定义一个kafka producer
    val producer = new KafkaProducer[String, String](properties)
    // 从文件中读取数据，发送
    val bufferedSource = io.Source.fromFile( "/Users/jimmyli/IdeaProjects/UserBehaviorAnalysis/HotItemsAnalysis/src/main/resources/UserBehavior.csv" )
    for( line <- bufferedSource.getLines() ){
      val record = new ProducerRecord[String, String](topic, line)
      producer.send(record)
    }
    producer.close()
  }
}
