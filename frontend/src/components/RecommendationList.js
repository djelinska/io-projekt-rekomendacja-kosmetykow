import React, { useEffect, useState } from 'react';

import ProductCard from './ProductCard';
import useFetch from '../useFetch';

const RecommendationList = ({
	selected_product_id,
	handleShowRecommendations,
}) => {
	const { fetchData, isLoading, error } = useFetch();
	const [recommendedProducts, setRecommendedProducts] = useState([]);

	useEffect(() => {
		const getRecommendedProducts = async () => {
			if (!isLoading) {
				const recommendedProducts = await fetchData(
					`/recommend?product_id=${selected_product_id}&recommendation_count=4`
				);
				setRecommendedProducts(recommendedProducts);
			}
		};

		getRecommendedProducts();
	}, []);

	return (
		<div className='fixed top-0 left-0 w-full h-full bg-zinc-700 bg-opacity-75 flex justify-center items-center'>
			<div className='max-w-fit p-8 bg-stone-50'>
				<div className='flex gap-6 justify-between items-center'>
					<h2 className='font-serif font-medium text-xl uppercase'>
						Recommended Products
					</h2>
					<button
						onClick={() => handleShowRecommendations(null)}
						className='w-8 h-8 font-sans rounded-full border border-stone-700'
					>
						X
					</button>
				</div>
				{isLoading && <div className='mt-6'>Loading...</div>}
				{error && <div className='mt-6'>{error}</div>}
				{recommendedProducts && !isLoading && (
					<div className='mt-6 flex flex-wrap gap-8'>
						{recommendedProducts.map((product) => (
							<React.Fragment key={product.product_id}>
								{product.product_id !== selected_product_id && (
									<div className='flex flex-col max-w-64'>
										<ProductCard product={product} />
									</div>
								)}
							</React.Fragment>
						))}
					</div>
				)}
			</div>
		</div>
	);
};

export default RecommendationList;
