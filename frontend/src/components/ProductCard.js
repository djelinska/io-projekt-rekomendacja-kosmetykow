const ProductCard = ({ product }) => {
	return (
		<>
			<div className='max-w-64 mx-auto'>
				<img
					src='cosmetics_product_example.jpg'
					alt='cosmetics product'
					className='rounded-full'
				/>
			</div>
			<div className='flex flex-col flex-1 mt-6'>
				<p className='text-sm'>
					{product.brand_name} &bull; {product.primary_category}
				</p>
				<div className='flex-1 my-2 flex gap-2'>
					<h3 className='font-serif font-medium text-lg leading-6'>
						{product.product_name}
					</h3>
					<span className='whitespace-nowrap'>
						&#x24; {parseFloat(product.price_usd).toFixed(2)}
					</span>
				</div>
				<p className='font-medium'>
					&#10022; {product.rating.toFixed(2)}
					<span className='text-sm font-normal ml-1'>
						&#x28;{parseInt(product.reviews)} ratings&#x29;
					</span>
				</p>
			</div>
		</>
	);
};

export default ProductCard;
