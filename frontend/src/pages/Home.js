import { useEffect, useState } from 'react';

import ProductList from '../components/ProductList';
import useFetch from '../useFetch';

const Home = () => {
	const { fetchData, isLoading, error } = useFetch();
	const [products, setProducts] = useState([]);

	useEffect(() => {
		const getProducts = async () => {
			if (!isLoading) {
				const products = await fetchData('/products');
				setProducts(products);
			}
		};

		getProducts();
	}, []);

	return (
		<div className='p-6'>
			{isLoading && <div>Loading...</div>}
			{error && <div>{error}</div>}
			{products && !isLoading && (
				<ProductList products={products}></ProductList>
			)}
		</div>
	);
};

export default Home;
