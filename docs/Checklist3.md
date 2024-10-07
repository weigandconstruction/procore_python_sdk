# Checklist3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**inspection_type** | [**InspectionType1**](InspectionType1.md) |  | [optional] 
**list_template_id** | **int** | Checklist Template ID | [optional] 
**name** | **str** | Name | [optional] 
**description** | **str** | Description | [optional] 
**distribution_members** | [**List[RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy]**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) | Users on the Inspection distribution list | [optional] 
**due_at** | **datetime** | Timestamp indicating when the Inspection is due | [optional] 
**identifier** | **str** | Identifier | [optional] 
**number** | **int** | Number | [optional] 
**status** | **str** | Status | [optional] 
**inspection_date** | **date** | Date that the inspection was performed | [optional] 
**created_at** | **datetime** | Timestamp of inspection creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**closed_at** | **datetime** | Timestamp of when inspection was closed | [optional] 
**item_count** | **int** | Checklist Item count | [optional] 
**yes_item_count** | **int** | Deprecated. Use &#x60;conforming_item_count&#x60; | [optional] 
**personal** | **bool** | Privacy status | [optional] 
**item_total** | **int** | (Deprecated) Use &#x60;item_count&#x60; | [optional] 
**conforming_item_count** | **int** | Count of Checklist Items with a status of &#x60;yes&#x60; | [optional] 
**deficient_item_count** | **int** | Count of Checklist Items with a status of &#x60;no&#x60; | [optional] 
**na_item_count** | **int** | Count of Checklist Items with a status of &#x60;n/a&#x60; | [optional] 
**neutral_item_count** | **int** | Number of Checklist Items with a status of &#x60;neutral&#x60; | [optional] 
**not_inspected_item_count** | **int** | Count of Checklist Items that have not been inspected | [optional] 
**drawing_ids** | **List[int]** | Array of Drawing IDs | [optional] 
**current_drawing_revision_ids** | **List[int]** | Array of Current Drawing Revision IDs | [optional] 
**location** | [**Location6**](Location6.md) |  | [optional] 
**specification_section** | [**Checklist3SpecificationSection**](Checklist3SpecificationSection.md) |  | [optional] 
**trade** | [**Trade2**](Trade2.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) |  | [optional] 
**closed_by** | [**ChecklistClosedBy**](ChecklistClosedBy.md) |  | [optional] 
**inspectors** | [**List[RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy]**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) | Checklist inspectors | [optional] 
**signature_requests** | [**List[ChecklistSignatureRequest2]**](ChecklistSignatureRequest2.md) | Checklist signature requests | [optional] 
**responsible_contractor** | [**Checklist3ResponsibleContractor**](Checklist3ResponsibleContractor.md) |  | [optional] 
**responsible_party** | [**ChecklistClosedBy**](ChecklistClosedBy.md) |  | [optional] 
**response_set** | [**ChecklistDefaultResponseSet1**](ChecklistDefaultResponseSet1.md) |  | [optional] 
**attachments** | [**List[Checklist3AttachmentsInner]**](Checklist3AttachmentsInner.md) | Checklist Attachments | [optional] 
**sections** | [**List[ChecklistSection]**](ChecklistSection.md) | Checklist Sections | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 
**managed_equipment_id** | **int** | Managed Equipment ID | [optional] 
**template_id** | **int** | Template ID | [optional] 
**list_template_name** | **str** | List Template Name | [optional] 
**trade_id** | **int** | Trade ID | [optional] 
**inspection_type_id** | **int** | Inspection Type ID | [optional] 

## Example

```python
from procore_sdk.models.checklist3 import Checklist3

# TODO update the JSON string below
json = "{}"
# create an instance of Checklist3 from a JSON string
checklist3_instance = Checklist3.from_json(json)
# print the JSON string representation of the object
print(Checklist3.to_json())

# convert the object into a dict
checklist3_dict = checklist3_instance.to_dict()
# create an instance of Checklist3 from a dict
checklist3_from_dict = Checklist3.from_dict(checklist3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


