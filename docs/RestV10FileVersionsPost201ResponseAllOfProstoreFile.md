# RestV10FileVersionsPost201ResponseAllOfProstoreFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Use :name, :filename to be deprecated | [optional] 
**url** | **str** |  | [optional] 
**filename** | **str** | :filename to be deprecated, use :name | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_file_versions_post201_response_all_of_prostore_file import RestV10FileVersionsPost201ResponseAllOfProstoreFile

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10FileVersionsPost201ResponseAllOfProstoreFile from a JSON string
rest_v10_file_versions_post201_response_all_of_prostore_file_instance = RestV10FileVersionsPost201ResponseAllOfProstoreFile.from_json(json)
# print the JSON string representation of the object
print(RestV10FileVersionsPost201ResponseAllOfProstoreFile.to_json())

# convert the object into a dict
rest_v10_file_versions_post201_response_all_of_prostore_file_dict = rest_v10_file_versions_post201_response_all_of_prostore_file_instance.to_dict()
# create an instance of RestV10FileVersionsPost201ResponseAllOfProstoreFile from a dict
rest_v10_file_versions_post201_response_all_of_prostore_file_from_dict = RestV10FileVersionsPost201ResponseAllOfProstoreFile.from_dict(rest_v10_file_versions_post201_response_all_of_prostore_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


