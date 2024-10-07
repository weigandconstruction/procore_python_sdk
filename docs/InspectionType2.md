# InspectionType2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**audit_transaction_timestamp** | **datetime** | Timestamp of audit | [optional] 
**source_id** | **int** |  | [optional] 
**deleted_at** | **datetime** | Timestamp of deletion | [optional] 
**company_id** | **int** | Company ID | [optional] 
**is_deletable** | **bool** | Is deletable | [optional] 

## Example

```python
from procore_sdk.models.inspection_type2 import InspectionType2

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionType2 from a JSON string
inspection_type2_instance = InspectionType2.from_json(json)
# print the JSON string representation of the object
print(InspectionType2.to_json())

# convert the object into a dict
inspection_type2_dict = inspection_type2_instance.to_dict()
# create an instance of InspectionType2 from a dict
inspection_type2_from_dict = InspectionType2.from_dict(inspection_type2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


