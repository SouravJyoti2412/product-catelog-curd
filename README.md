
## Product Catelog all route 

## perpose product create 
route => http://127.0.0.1:8000/product-curd/ , httpMthod => post ,  params => {"product_name":"hero shine ","description":"bike have some issue","price":130000,"inventory_count":3,"category":"commuter"}

## perpose product update
route => http://127.0.0.1:8000/product-curd/ , httpMthod => put ,  params => {id ="3","product_name":"hero shine ","description":"bike have some issue","price":130000,"inventory_count":3,"category":"commuter"}

## perpose product delete
route => http://127.0.0.1:8000/product-curd/ , httpMethod => delete ,  params => {id ="3"}

## perpose all product view 
route => http://127.0.0.1:8000/product-curd/ , httpMethod => get ,  params => {}

## product buy 
route => http://127.0.0.1:8000/product-buy/ , httpMethod => post ,  params => {"id":2,"product_quantity":2}

## product search 
route => http://127.0.0.1:8000/product-search/ , httpMethod => get ,  params => {query:vichle}

## product popularity low to High
route => http://127.0.0.1:8000/product-popularity-low-to-high/ , httpMethod => get ,  params => {}

## product popularity High to Low
route => http://127.0.0.1:8000/product-popularity-high-to-low/ , httpMethod => get ,  params => {}

# Build the Docker images
docker-compose build

# Start the Docker containers
docker-compose up



