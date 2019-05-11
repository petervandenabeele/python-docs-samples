# -*- coding: utf-8 -*-
#
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# DO NOT EDIT! This is a generated sample ("Request",  "job_search_create_job")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-talent

import sys

# [START job_search_create_job]

from google.cloud import talent_v4beta1
import six


def sample_create_job(project_id, tenant_id, company_name, requisition_id,
                      title, description, job_application_url, address_one,
                      address_two, language_code):
    """Create Job"""
    # [START job_search_create_job_core]

    client = talent_v4beta1.JobServiceClient()

    # project_id = 'Your Google Cloud Project ID'
    # tenant_id = 'Your Tenant ID (using tenancy is optional)'
    # company_name = 'Company name, e.g. projects/your-project/companies/company-id'
    # requisition_id = 'Job requisition ID, aka Posting ID. Unique per job.'
    # title = 'Software Engineer'
    # description = 'This is a description of this <i>wonderful</i> job!'
    # job_application_url = 'https://www.example.org/job-posting/123'
    # address_one = '1600 Amphitheatre Parkway, Mountain View, CA 94043'
    # address_two = '111 8th Avenue, New York, NY 10011'
    # language_code = 'en-US'

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode('utf-8')
    if isinstance(tenant_id, six.binary_type):
        tenant_id = tenant_id.decode('utf-8')
    if isinstance(company_name, six.binary_type):
        company_name = company_name.decode('utf-8')
    if isinstance(requisition_id, six.binary_type):
        requisition_id = requisition_id.decode('utf-8')
    if isinstance(title, six.binary_type):
        title = title.decode('utf-8')
    if isinstance(description, six.binary_type):
        description = description.decode('utf-8')
    if isinstance(job_application_url, six.binary_type):
        job_application_url = job_application_url.decode('utf-8')
    if isinstance(address_one, six.binary_type):
        address_one = address_one.decode('utf-8')
    if isinstance(address_two, six.binary_type):
        address_two = address_two.decode('utf-8')
    if isinstance(language_code, six.binary_type):
        language_code = language_code.decode('utf-8')
    parent = client.tenant_path(project_id, tenant_id)
    uris = [job_application_url]
    application_info = {'uris': uris}
    addresses = [address_one, address_two]
    job = {
        'company': company_name,
        'requisition_id': requisition_id,
        'title': title,
        'description': description,
        'application_info': application_info,
        'addresses': addresses,
        'language_code': language_code
    }

    response = client.create_job(parent, job)
    print('Created job: {}'.format(response.name))

    # [END job_search_create_job_core]


# [END job_search_create_job]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--project_id',
                        type=str,
                        default='Your Google Cloud Project ID')
    parser.add_argument('--tenant_id',
                        type=str,
                        default='Your Tenant ID (using tenancy is optional)')
    parser.add_argument(
        '--company_name',
        type=str,
        default='Company name, e.g. projects/your-project/companies/company-id'
    )
    parser.add_argument(
        '--requisition_id',
        type=str,
        default='Job requisition ID, aka Posting ID. Unique per job.')
    parser.add_argument('--title', type=str, default='Software Engineer')
    parser.add_argument(
        '--description',
        type=str,
        default='This is a description of this <i>wonderful</i> job!')
    parser.add_argument('--job_application_url',
                        type=str,
                        default='https://www.example.org/job-posting/123')
    parser.add_argument(
        '--address_one',
        type=str,
        default='1600 Amphitheatre Parkway, Mountain View, CA 94043')
    parser.add_argument('--address_two',
                        type=str,
                        default='111 8th Avenue, New York, NY 10011')
    parser.add_argument('--language_code', type=str, default='en-US')
    args = parser.parse_args()

    sample_create_job(args.project_id, args.tenant_id, args.company_name,
                      args.requisition_id, args.title, args.description,
                      args.job_application_url, args.address_one,
                      args.address_two, args.language_code)


if __name__ == '__main__':
    main()