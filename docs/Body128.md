# Body128


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**view** | **str** | Specify response schema view | [optional] 
**bim_model** | [**Body128BimModel**](Body128BimModel.md) |  | 

## Example

```python
from procore_sdk.models.body128 import Body128

# TODO update the JSON string below
json = "{}"
# create an instance of Body128 from a JSON string
body128_instance = Body128.from_json(json)
# print the JSON string representation of the object
print(Body128.to_json())

# convert the object into a dict
body128_dict = body128_instance.to_dict()
# create an instance of Body128 from a dict
body128_from_dict = Body128.from_dict(body128_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


