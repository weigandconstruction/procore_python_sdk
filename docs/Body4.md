# Body4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**contract_detail_line_item** | [**Body4ContractDetailLineItem**](Body4ContractDetailLineItem.md) |  | 

## Example

```python
from procore_sdk.models.body4 import Body4

# TODO update the JSON string below
json = "{}"
# create an instance of Body4 from a JSON string
body4_instance = Body4.from_json(json)
# print the JSON string representation of the object
print(Body4.to_json())

# convert the object into a dict
body4_dict = body4_instance.to_dict()
# create an instance of Body4 from a dict
body4_from_dict = Body4.from_dict(body4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


