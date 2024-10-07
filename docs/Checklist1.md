# Checklist1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**list_template_id** | **int** | Checklist Template ID | [optional] 
**name** | **str** | Name | [optional] 
**list_template_name** | **str** | Name of the Template the Inspection was created from | [optional] 
**description** | **str** | Description | [optional] 
**distribution_members** | [**List[RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy]**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) | Users on the Inspection distribution list | [optional] 
**due_at** | **datetime** | Timestamp indicating when the Inspection is due | [optional] 
**number** | **int** | Number | [optional] 
**status** | **str** | Status | [optional] 
**identifier** | **str** | Identifier | [optional] 
**inspection_date** | **date** | Date that the inspection was performed | [optional] 
**created_at** | **datetime** | Timestamp of inspection creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 
**closed_at** | **datetime** | Timestamp of when inspection was closed | [optional] 
**item_count** | **int** | Checklist Item count | [optional] 
**yes_item_count** | **int** | (Deprecated) Use &#x60;conforming_item_count&#x60; | [optional] 
**personal** | **bool** | Checklist personal status | [optional] 
**item_total** | **int** | (Deprecated) Use &#x60;item_count&#x60; | [optional] 
**conforming_item_count** | **int** | Count of Checklist Items with a status of &#x60;yes&#x60; | [optional] 
**deficient_item_count** | **int** | Count of Checklist Items with a status of &#x60;no&#x60; | [optional] 
**na_item_count** | **int** | Count of Checklist Items with a status of &#x60;n/a&#x60; | [optional] 
**neutral_item_count** | **int** | Number of Checklist Items with a status of &#x60;neutral&#x60; | [optional] 
**not_inspected_item_count** | **int** | Count of Checklist Items that have not been inspected | [optional] 
**drawing_ids** | **List[int]** | Array of Drawing IDs | [optional] 
**current_drawing_revision_ids** | **List[int]** | Array of Current Drawing Revision IDs | [optional] 
**attachments** | [**List[Checklist1AttachmentsInner]**](Checklist1AttachmentsInner.md) | Checklist attachments | [optional] 
**created_by** | [**RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) |  | [optional] 
**closed_by** | [**ChecklistClosedBy**](ChecklistClosedBy.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**specification_section** | [**Checklist1SpecificationSection**](Checklist1SpecificationSection.md) |  | [optional] 
**signature_requests** | [**List[ChecklistSignatureRequest1]**](ChecklistSignatureRequest1.md) | Checklist signature requests | [optional] 
**trade** | [**Trade**](Trade.md) |  | [optional] 
**inspectors** | [**List[RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy]**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) | Users that will be performing the inspection | [optional] 
**responsible_contractor** | [**Checklist1ResponsibleContractor**](Checklist1ResponsibleContractor.md) |  | [optional] 
**responsible_party** | [**RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy**](RestV10ProjectsProjectIdChecklistListTemplatesPost201ResponseAllOfCreatedBy.md) |  | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 
**managed_equipment_id** | **int** | Managed Equipment ID | [optional] 

## Example

```python
from procore_sdk.models.checklist1 import Checklist1

# TODO update the JSON string below
json = "{}"
# create an instance of Checklist1 from a JSON string
checklist1_instance = Checklist1.from_json(json)
# print the JSON string representation of the object
print(Checklist1.to_json())

# convert the object into a dict
checklist1_dict = checklist1_instance.to_dict()
# create an instance of Checklist1 from a dict
checklist1_from_dict = Checklist1.from_dict(checklist1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


