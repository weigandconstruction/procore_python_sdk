# RFQResponse2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**comment** | **str** | Comment in response to the latest quote | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**prostore_file_ids** | **List[int]** | Prostore file IDs | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rfq_response2 import RFQResponse2

# TODO update the JSON string below
json = "{}"
# create an instance of RFQResponse2 from a JSON string
rfq_response2_instance = RFQResponse2.from_json(json)
# print the JSON string representation of the object
print(RFQResponse2.to_json())

# convert the object into a dict
rfq_response2_dict = rfq_response2_instance.to_dict()
# create an instance of RFQResponse2 from a dict
rfq_response2_from_dict = RFQResponse2.from_dict(rfq_response2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


