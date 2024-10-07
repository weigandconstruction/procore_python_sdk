# WbsCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Wbs Code ID | [optional] 
**flat_code** | **str** | Wbs Code | [optional] 
**description** | **str** | Wbs Code Description | [optional] 

## Example

```python
from procore_sdk.models.wbs_code import WbsCode

# TODO update the JSON string below
json = "{}"
# create an instance of WbsCode from a JSON string
wbs_code_instance = WbsCode.from_json(json)
# print the JSON string representation of the object
print(WbsCode.to_json())

# convert the object into a dict
wbs_code_dict = wbs_code_instance.to_dict()
# create an instance of WbsCode from a dict
wbs_code_from_dict = WbsCode.from_dict(wbs_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


