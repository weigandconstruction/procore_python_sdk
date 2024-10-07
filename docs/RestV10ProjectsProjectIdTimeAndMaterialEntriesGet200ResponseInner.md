# RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner

Time and Material Entry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | The title of T&amp;M ticket | [optional] 
**reference_number** | **str** | The refrence number associate with T&amp;M ticket | [optional] 
**description** | **str** | The description of job | [optional] 
**status** | **int** | Current status of T&amp;M ticket | [optional] 
**private** | **bool** | If the T&amp;M ticket is private | [optional] 
**number** | **int** | Unique number for the T&amp;M ticket | [optional] 
**company_signee_party** | [**ExtendedView**](ExtendedView.md) |  | [optional] 
**company_signature** | [**RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerCompanySignature**](RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerCompanySignature.md) |  | [optional] 
**customer_signature** | [**RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerCustomerSignature**](RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerCustomerSignature.md) |  | [optional] 
**customer_signee_party** | [**ExtendedView1**](ExtendedView1.md) |  | [optional] 
**project_id** | **int** | ID of the project the T&amp;M ticket was logged for | [optional] 
**company_id** | **int** | ID of the company the T&amp;M ticket was logged for | [optional] 
**location_id** | **int** | ID of the location the T&amp;M ticket was logged for | [optional] 
**customer_id** | **int** | ID of the costomer who asked for T&amp;M ticket | [optional] 
**work_performed_on_date** | **str** | Date work performed on | [optional] 
**updated_at** | **datetime** | Date the T&amp;M ticket was updated | [optional] 
**created_at** | **datetime** | Date the T&amp;M ticket was created | [optional] 
**deleted_at** | **datetime** | Date the T&amp;M ticket was deleted | [optional] 
**created_by_id** | **int** | The user ID the T&amp;M ticket was created with | [optional] 
**time_and_material_entry_attachments** | [**List[RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner]**](RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInnerTimeAndMaterialEntryAttachmentsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_entries_get200_response_inner import RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner from a JSON string
rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_instance = RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_dict = rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner from a dict
rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_from_dict = RestV10ProjectsProjectIdTimeAndMaterialEntriesGet200ResponseInner.from_dict(rest_v10_projects_project_id_time_and_material_entries_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


