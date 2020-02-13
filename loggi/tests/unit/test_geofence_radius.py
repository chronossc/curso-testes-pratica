import pytest

def get_checkin_geofence_radius(veiculo):
	"""
	Moto 600m
	Van 1500m
	Outros 743,59
	"""
	return {
		'moto': 600,
		'van': 1500
	}.get(veiculo, 743.59)


@pytest.fixture(
	params=[
		(0, True),
		(1, True),
		(559, True),
		(600, True),
		(601, False),
	]
)
def moto(request):
	return request.param


@pytest.fixture(
	params=[
		(0, True),
		(1, True),
		(1499, True),
		(1500, True),
		(1501, False),
	]
)
def van(request):
	return request.param
	

@pytest.fixture(
	params=[
		(0, True),
		(1, True),
		(743, True),
		(743.59, True),
		(744, False),
	]
)
def outro(request):
	return request.param
	

def test_moto(moto):
	v, expected = moto
	max_distance = get_checkin_geofence_radius('moto')
	assert (v <= max_distance) is expected


def test_van(van):
	v, expected = van
	max_distance = get_checkin_geofence_radius('van')
	assert (v <= max_distance) is expected


def test_outro(outro):
	v, expected = outro
	max_distance = get_checkin_geofence_radius('outro')
	assert (v <= max_distance) is expected

