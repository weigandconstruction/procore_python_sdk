# RFQ1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_id** | **int** | Assigned ID | [optional] 
**change_event_event_id** | **int** | Change Event ID | [optional] 
**cost_code_id** | **int** | Cost Code ID | [optional] 
**description** | **str** | Description | [optional] 
**due_date** | **date** | Due date | [optional] 
**estimated_amount** | **float** | Estimated amount | [optional] 
**estimated_schedule_impact** | **int** | Estimated schedule impact in days | [optional] 
**estimated_status** | **str** | Estimated status | [optional] 
**location_id** | **int** | Location ID | [optional] 
**number** | **str** | Number | [optional] 
**original_quote** | **float** | Original quote | [optional] 
**private** | **bool** | If true, visible to admins only; otherwise visible to those with access to the parent contract. | [optional] [default to False]
**spec_section_description** | **str** | Specification Section description | [optional] 
**spec_section_number** | **str** | Specification Section number | [optional] 
**specification_section_id** | **int** | Specification Section ID | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | 
**prostore_file_ids** | **List[int]** | Prostore File IDs | [optional] 

## Example

```python
from procore_sdk.models.rfq1 import RFQ1

# TODO update the JSON string below
json = "{}"
# create an instance of RFQ1 from a JSON string
rfq1_instance = RFQ1.from_json(json)
# print the JSON string representation of the object
print(RFQ1.to_json())

# convert the object into a dict
rfq1_dict = rfq1_instance.to_dict()
# create an instance of RFQ1 from a dict
rfq1_from_dict = RFQ1.from_dict(rfq1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


