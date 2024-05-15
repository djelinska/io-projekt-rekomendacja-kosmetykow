import { useState } from 'react';

const useFetch = () => {
	const [isLoading, setIsLoading] = useState(false);
	const [error, setError] = useState('');

	const fetchData = async (endpoint) => {
		setIsLoading(true);

		const res = await fetch('http://localhost:5000' + endpoint);
		const resBody = await res.json();

		if (!res.ok) {
			setIsLoading(false);
			setError(resBody.error);
		} else {
			setIsLoading(false);
			return resBody;
		}
	};

	return { fetchData, isLoading, error };
};

export default useFetch;
