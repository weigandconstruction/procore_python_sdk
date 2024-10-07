# BIMLevelBatchCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bim_levels** | [**List[RestV10BimLevelsGet200ResponseInner]**](RestV10BimLevelsGet200ResponseInner.md) |  | [optional] 
**errors** | [**List[BIMLevelBatchCreateResponseErrorsInner]**](BIMLevelBatchCreateResponseErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.bim_level_batch_create_response import BIMLevelBatchCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BIMLevelBatchCreateResponse from a JSON string
bim_level_batch_create_response_instance = BIMLevelBatchCreateResponse.from_json(json)
# print the JSON string representation of the object
print(BIMLevelBatchCreateResponse.to_json())

# convert the object into a dict
bim_level_batch_create_response_dict = bim_level_batch_create_response_instance.to_dict()
# create an instance of BIMLevelBatchCreateResponse from a dict
bim_level_batch_create_response_from_dict = BIMLevelBatchCreateResponse.from_dict(bim_level_batch_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


