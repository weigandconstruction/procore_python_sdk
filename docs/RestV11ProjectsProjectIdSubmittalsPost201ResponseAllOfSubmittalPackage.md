# RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfSubmittalPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments_count** | **int** |  | [optional] 
**created_by** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 
**description** | **str** |  | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 
**submittal_ids** | **List[int]** |  | [optional] 
**id** | **int** |  | [optional] 
**number** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_submittals_post201_response_all_of_submittal_package import RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfSubmittalPackage

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfSubmittalPackage from a JSON string
rest_v11_projects_project_id_submittals_post201_response_all_of_submittal_package_instance = RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfSubmittalPackage.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfSubmittalPackage.to_json())

# convert the object into a dict
rest_v11_projects_project_id_submittals_post201_response_all_of_submittal_package_dict = rest_v11_projects_project_id_submittals_post201_response_all_of_submittal_package_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfSubmittalPackage from a dict
rest_v11_projects_project_id_submittals_post201_response_all_of_submittal_package_from_dict = RestV11ProjectsProjectIdSubmittalsPost201ResponseAllOfSubmittalPackage.from_dict(rest_v11_projects_project_id_submittals_post201_response_all_of_submittal_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


