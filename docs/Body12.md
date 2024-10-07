# Body12


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | 
**updates** | [**List[Body12UpdatesInner]**](Body12UpdatesInner.md) |  | 

## Example

```python
from procore_sdk.models.body12 import Body12

# TODO update the JSON string below
json = "{}"
# create an instance of Body12 from a JSON string
body12_instance = Body12.from_json(json)
# print the JSON string representation of the object
print(Body12.to_json())

# convert the object into a dict
body12_dict = body12_instance.to_dict()
# create an instance of Body12 from a dict
body12_from_dict = Body12.from_dict(body12_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


