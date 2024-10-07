# RestV10FileVersionsPostRequestFileVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the file when downloaded | [optional] 
**notes** | **str** | Notes about the File Version | [optional] 
**data** | **str** | File to use as file data. Note that it&#39;s only possible to post a file using a multipart/form-data body (see RFC 2388). Most HTTP libraries will do the right thing when you pass in an open file or IO stream. Alternatively you can use an upload_uuid (see Company Uploads or Project Uploads). You should not use both file and upload_uuid fields in the same request. | 
**upload_uuid** | **str** | UUID referencing a previously completed Upload. See Company Uploads or Project Uploads for instructions on how use uploads. You should not use both data and upload_uuid fields in the same request. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_file_versions_post_request_file_version import RestV10FileVersionsPostRequestFileVersion

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10FileVersionsPostRequestFileVersion from a JSON string
rest_v10_file_versions_post_request_file_version_instance = RestV10FileVersionsPostRequestFileVersion.from_json(json)
# print the JSON string representation of the object
print(RestV10FileVersionsPostRequestFileVersion.to_json())

# convert the object into a dict
rest_v10_file_versions_post_request_file_version_dict = rest_v10_file_versions_post_request_file_version_instance.to_dict()
# create an instance of RestV10FileVersionsPostRequestFileVersion from a dict
rest_v10_file_versions_post_request_file_version_from_dict = RestV10FileVersionsPostRequestFileVersion.from_dict(rest_v10_file_versions_post_request_file_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


