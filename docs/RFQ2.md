# RFQ2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**commitment_contract_id** | **int** | Commitment Contract ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**description** | **str** | Description | [optional] 
**due_date** | **date** | Due date | [optional] 
**estimated_amount** | **float** | Estimated amount | [optional] 
**estimated_schedule_impact** | **int** | Estimated schedule impact in days | [optional] 
**estimated_status** | **str** | Estimated status | [optional] 
**intent_to_quote** | **bool** | Intent to quote status | [optional] 
**number** | **str** | Number | [optional] 
**original_quote** | **float** | Original quote | [optional] 
**position** | **int** | Position | [optional] 
**private** | **bool** | If true, visible to admins only; otherwise visible to those with access to the parent contract. | [optional] 
**prostore_file_ids** | **List[int]** | Prostore File IDs | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**specification_section** | [**RFQSpecificationSection**](RFQSpecificationSection.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**assigned** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**cost_code** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rfq2 import RFQ2

# TODO update the JSON string below
json = "{}"
# create an instance of RFQ2 from a JSON string
rfq2_instance = RFQ2.from_json(json)
# print the JSON string representation of the object
print(RFQ2.to_json())

# convert the object into a dict
rfq2_dict = rfq2_instance.to_dict()
# create an instance of RFQ2 from a dict
rfq2_from_dict = RFQ2.from_dict(rfq2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


