import pytest
import testapp as app

# whenever the decorated function is used, it’ll be used with every parameter, 
# so just calling generate_initial_transform_parameters will call it twice, once with nodict as a parameter and once with dict
@pytest.fixture(params=['nodict', 'dict']) # decorator to declare the following function definition a fixture
def generate_initial_transform_parameters(request): # named parameter params to use with generate_initial_transform_parameters
    # add the pytest special object request to our function signature to access parameters
    
    # set up the input and expected output
    test_input = {
        'name': 'John Q. Public',
        'street': '123 Main St.',
        'city': 'Anytown',
        'state': 'FL',
        'zip': 99999,
    }
    expected_output = {
        'name': 'John Q. Public',
        'street': '123 Main St.',
        'city': 'Anytown',
        'state': 'FL',
        'zip': 99999,
    }

    # if we have the 'dict' parameter, then we modify the input and expected ouput, allowing us to test the if block
    if request.param == 'dict':
        test_input['relastionships'] = {
            'siblings': ['Michael R. Public', 'Suzy Q. Public'],
            'parents': ['John Q. Public Sr.', 'Mary S. Public'],
        }
        expected_output['siblings'] = ['Michael R. Public', 'Suzy Q. Public']
        expected_output['parents'] = ['John Q. Public Sr.', 'Mary S. Public']
    
    return test_input, expected_output

# write the test
# we have to pass the fixture to the test function as a parameter to have access to it
def test_initial_transform(generate_initial_transform_parameters):
    test_input = generate_initial_transform_parameters[0]
    expected_output = generate_initial_transform_parameters[1]
    assert app.initial_transform(test_input) == expected_output