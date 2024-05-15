import ProductCard from './ProductCard';
import RecommendationList from './RecommendationList';
import { useState } from 'react';

const ProductList = ({ products }) => {
	const [selectedProductId, setSelectedProductId] = useState(null);

	const handleShowRecommendations = (product_id) => {
		setSelectedProductId(product_id);
	};

	return (
		<div className='max-w-screen-lg m-auto'>
			<h1 className='mb-6 font-serif font-medium text-2xl uppercase'>
				All Products
			</h1>
			<div className='grid grid-cols-3 gap-8'>
				{products.map((product) => (
					<div key={product.product_id} className='flex flex-col'>
						<ProductCard product={product} />
						<button
							onClick={() => handleShowRecommendations(product.product_id)}
							className='mt-6 p-1 font-sans rounded-full border border-stone-700 text-sm uppercase'
						>
							You might also like &#x25BE;
						</button>
						{selectedProductId === product.product_id && (
							<RecommendationList
								selected_product_id={product.product_id}
								handleShowRecommendations={handleShowRecommendations}
							/>
						)}
					</div>
				))}
			</div>
		</div>
	);
};

export default ProductList;
