# RestV10ProjectsProjectIdBidPackagesPost201ResponseManager


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_information_id** | **int** | Login Information ID | [optional] 
**contact_id** | **int** | Contact ID | [optional] 
**name** | **str** | Manager Name | [optional] 
**email** | **str** | Manager Email | [optional] 
**job_title** | **str** | Manager Job Title | [optional] 
**invited** | **bool** | User Invited | [optional] 
**vendor** | [**RestV10ProjectsProjectIdBidPackagesPost201ResponseManagerVendor**](RestV10ProjectsProjectIdBidPackagesPost201ResponseManagerVendor.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_bid_packages_post201_response_manager import RestV10ProjectsProjectIdBidPackagesPost201ResponseManager

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdBidPackagesPost201ResponseManager from a JSON string
rest_v10_projects_project_id_bid_packages_post201_response_manager_instance = RestV10ProjectsProjectIdBidPackagesPost201ResponseManager.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdBidPackagesPost201ResponseManager.to_json())

# convert the object into a dict
rest_v10_projects_project_id_bid_packages_post201_response_manager_dict = rest_v10_projects_project_id_bid_packages_post201_response_manager_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdBidPackagesPost201ResponseManager from a dict
rest_v10_projects_project_id_bid_packages_post201_response_manager_from_dict = RestV10ProjectsProjectIdBidPackagesPost201ResponseManager.from_dict(rest_v10_projects_project_id_bid_packages_post201_response_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


