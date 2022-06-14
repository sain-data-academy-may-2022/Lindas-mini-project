CREATE TABLE `courier` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `phone` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
);


CREATE TABLE `customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `phone` int NOT NULL,
  PRIMARY KEY (`id`)
);


CREATE TABLE `order` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int NOT NULL,
  `courier_id` int NOT NULL,
  `status` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  KEY `courier_id` (`courier_id`),
  CONSTRAINT `order_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
  CONSTRAINT `order_ibfk_2` FOREIGN KEY (`courier_id`) REFERENCES `courier` (`id`)
);


CREATE TABLE `order_product` (
  `product_id` int NOT NULL,
  `order_id` int NOT NULL,
  KEY `product_id` (`product_id`),
  KEY `order_id` (`order_id`),
  CONSTRAINT `order_product_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`),
  CONSTRAINT `order_product_ibfk_2` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`)
);


CREATE TABLE `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`id`)
);