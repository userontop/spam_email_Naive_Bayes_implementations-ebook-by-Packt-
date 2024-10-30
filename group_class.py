def get_prior(label_index):
	"""	Compute prior based on training samples
	Args:
		label_index (grouped sample indices by class)
	Returns:
		dictionary, with class label as key, corresponding prior as the value
	"""
	prior = {label: len(index) for label, index in label_index.items()}
	total_count = sum(prior.values())
	for label in prior:
		prior[label] /= float(total_count)
	return prior
