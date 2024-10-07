# Body110


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | The ID of the Company the Office belongs to | 
**office** | [**Office2**](Office2.md) |  | 

## Example

```python
from procore_sdk.models.body110 import Body110

# TODO update the JSON string below
json = "{}"
# create an instance of Body110 from a JSON string
body110_instance = Body110.from_json(json)
# print the JSON string representation of the object
print(Body110.to_json())

# convert the object into a dict
body110_dict = body110_instance.to_dict()
# create an instance of Body110 from a dict
body110_from_dict = Body110.from_dict(body110_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


