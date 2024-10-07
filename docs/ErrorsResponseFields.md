# ErrorsResponseFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Errors for the given field where the key is the inputted label and the value is the error string | [optional] 

## Example

```python
from procore_sdk.models.errors_response_fields import ErrorsResponseFields

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorsResponseFields from a JSON string
errors_response_fields_instance = ErrorsResponseFields.from_json(json)
# print the JSON string representation of the object
print(ErrorsResponseFields.to_json())

# convert the object into a dict
errors_response_fields_dict = errors_response_fields_instance.to_dict()
# create an instance of ErrorsResponseFields from a dict
errors_response_fields_from_dict = ErrorsResponseFields.from_dict(errors_response_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


